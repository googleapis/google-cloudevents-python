#!/usr/bin/env node
const yargs = require('yargs');
const mkdirp = require('mkdirp');
const fs = require('fs');
const sqrl = require('squirrelly');

const qt = require('qt');

let IN = yargs.argv.in || process.env.IN;
let OUT = yargs.argv.out || process.env.OUT;
let EXAMPLES = yargs.argv.examples || process.env.EXAMPLES

const LANGUAGE = 'python';
const SRC_DIRECTORY = 'src';
const TEMPLATE_DIRECTORY = 'templates';
const INIT_PY_TEMPLATE = 'init_py.squirrelly';
const README_TEMPLATE = 'README.squirrelly';
const SETUP_PY_TEMPLATE = 'setup_py.squirrelly';
const DISCLAIMER_TEMPLATE = 'disclaimer';
const VERSION = '0.0.1';
const EXAMPLE_PATH_PREFIX = 'https://googleapis.github.io/google-cloudevents/testdata/';
const PY_TEST_TEMPLATE = 'pytest.squirrelly';
const PY_TEST_HELPER_TEMPLATE = 'pytest_helper.squirrelly';
const PACKAGE_PREFIX = 'google.events.'
const TEST_DIRECTORY = 'tests';
const TEST_DATA_DIRECTORY = 'data';

interface Event {
  package: string;
  eventName: string;
  eventDescription: string;
}

async function main() {
  if (!IN) console.error('Error in config: `IN` not set');
  if (!OUT) console.error('Error in config: `OUT` not set');
  if (!IN || !OUT) return;
  if (!EXAMPLES) console.warn('Warn in config: `EXAMPLES` not set');
  if (IN.endsWith('/')) IN = IN.substring(0, IN.length - 1);
  if (OUT.endsWith('/')) OUT = OUT.substring(0, OUT.length - 1);
  if (EXAMPLES && EXAMPLES.endsWith('/')) EXAMPLES = EXAMPLES.substring(0, EXAMPLES.length - 1);

  const templateDirectoryPath = `${__dirname}/../../${TEMPLATE_DIRECTORY}`;

  const schemasAndGenFiles = await qt.getJSONSchemasAndGenFiles(IN, LANGUAGE);
  const allEventsByPkg: Map<string, Event[]> = new Map<string, Event[]>();
  const disclaimer: string = fs.readFileSync(
    `${templateDirectoryPath}/${DISCLAIMER_TEMPLATE}`
  );
  schemasAndGenFiles.map(([schema, genFile]: [any, string]) => {
    // Collect package information and its path
    const pkg = schema['package'];
    const pkgPath = pkg.replace(/\./g, '/');

    // Create directories as needed
    mkdirp.sync(`${OUT}/${SRC_DIRECTORY}/${pkgPath}`);
    mkdirp.sync(`${OUT}/${TEST_DIRECTORY}/${TEST_DATA_DIRECTORY}`);

    // Write generated Python scripts
    const eventName = schema.name;
    fs.writeFileSync(
      `${OUT}/${SRC_DIRECTORY}/${pkgPath}/${eventName}.py`,
      disclaimer + genFile
    );
    
    // Copy event data examples
    const examplePaths: string[] = [];
    for (const examplePath of schema.examples) {
      const examplePathWithoutPrefix = examplePath.replace(EXAMPLE_PATH_PREFIX, '');
      examplePaths.push(examplePathWithoutPrefix);
    }
    const exampleNames: string[] = [];
    for (const examplePath of examplePaths) {
      const exampleName = examplePath
        .replace('.json', '')
        .replace(/\//g, '.')
        .replace(PACKAGE_PREFIX, '')
        .replace(/\./g, '_')
        .replace(/\-/g, '_')
        .toLowerCase();
      exampleNames.push(exampleName);
      fs.copyFileSync(`${EXAMPLES}/${examplePath}`, `${OUT}/${TEST_DIRECTORY}/${TEST_DATA_DIRECTORY}/${exampleName}.json`);
    }

    // Collect event related information
    const eventDescription = schema.description.replace(/\n/g, '');
    const event = {
      package: pkg,
      eventName: eventName,
      eventDescription: eventDescription,
      examples: exampleNames,
    };

    // Collect each event and categorize by the package it belongs to
    if (allEventsByPkg.has(pkg)) {
      const pkgEvents = allEventsByPkg.get(pkg);
      pkgEvents?.push(event);
    } else {
      const pkgEvents: Event[] = [event];
      allEventsByPkg.set(pkg, pkgEvents);
    }
  });

  // Write __init__.py scripts
  const initPySqrlTmpl = fs.readFileSync(
    `${templateDirectoryPath}/${INIT_PY_TEMPLATE}`
  );
  for (const pkg of allEventsByPkg.keys()) {
    const pkgEvents = allEventsByPkg.get(pkg);
    const pkgPath = pkg.replace(/\./g, '/');
    const initPy = sqrl.render(String(initPySqrlTmpl), {
      pkgEvents: pkgEvents,
    });
    fs.writeFileSync(`${OUT}/${SRC_DIRECTORY}/${pkgPath}/__init__.py`, initPy);
  }

  // Write the README.md file
  const readMeSqrlTmpl = fs.readFileSync(
    `${templateDirectoryPath}/${README_TEMPLATE}`
  );
  const allEvents = Array.from(allEventsByPkg.values());
  const readMe = sqrl.render(String(readMeSqrlTmpl), {
    allEvents: allEvents,
  });
  fs.writeFileSync(`${OUT}/README.md`, readMe);

  // Write the setup.py script
  const setupPySqrlTmpl = fs.readFileSync(
    `${templateDirectoryPath}/${SETUP_PY_TEMPLATE}`
  );
  const setupPy = sqrl.render(String(setupPySqrlTmpl), {
    srcDirectory: SRC_DIRECTORY,
    version: VERSION,
  });
  fs.writeFileSync(`${OUT}/setup.py`, setupPy);

  // Generate the tests
  const pyTestTmpl = fs.readFileSync(
    `${templateDirectoryPath}/${PY_TEST_TEMPLATE}`
  );
  const pyTestHelperTmpl = fs.readFileSync(
    `${templateDirectoryPath}/${PY_TEST_HELPER_TEMPLATE}`
  );
  const pyTestHelper = sqrl.render(String(pyTestHelperTmpl));
  fs.writeFileSync(`${OUT}/${TEST_DIRECTORY}/helper.py`, pyTestHelper);
  for (const pkg of allEventsByPkg.keys()) {
    const pkgEvents = allEventsByPkg.get(pkg);
    const pkgWithoutPrefix = pkg.replace(PACKAGE_PREFIX, '').replace(/\./g, '_').toLowerCase();
    const pytest = sqrl.render(String(pyTestTmpl), {
      pkgEvents: pkgEvents,
      testDirectory: TEST_DIRECTORY,
      testDataDirectory: TEST_DATA_DIRECTORY,
    });
    fs.writeFileSync(
      `${OUT}/${TEST_DIRECTORY}/test_${pkgWithoutPrefix}.py`,
      pytest
    );
  }
}

if (!module.parent) {
  main();
}
