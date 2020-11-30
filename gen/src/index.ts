#!/usr/bin/env node
const yargs = require('yargs');
const mkdirp = require('mkdirp');
const fs = require('fs');
const sqrl = require('squirrelly');

const qt = require('qt');

let IN = yargs.argv.in || process.env.IN;
let OUT = yargs.argv.out || process.env.OUT;

const LANGUAGE = 'python';
const SRC_DIRECTORY = 'src';
const TEMPLATE_DIRECTORY = 'templates';
const INIT_PY_TEMPLATE = 'init_py.squirrelly';
const README_TEMPLATE = 'README.squirrelly';
const SETUP_PY_TEMPLATE = 'setup_py.squirrelly';
const DISCLAIMER_TEMPLATE = 'disclaimer';
const VERSION = '0.0.1';

interface Event {
  package: string;
  eventName: string;
  eventDescription: string;
}

async function main() {
  if (!IN) console.error('Error in config: `IN` not set');
  if (!OUT) console.error('Error in config: `OUT` not set');
  if (!IN || !OUT) return;
  if (IN.endsWith('/')) IN = IN.substring(0, IN.length - 1);
  if (OUT.endsWith('/')) OUT = OUT.substring(0, OUT.length - 1);

  const templateDirectoryPath = `${__dirname}/../../${TEMPLATE_DIRECTORY}`;

  const schemasAndGenFiles = await qt.getJSONSchemasAndGenFiles(IN, LANGUAGE);
  const allEventsByPkg: Map<string, Event[]> = new Map<string, Event[]>();
  const disclaimer: string = fs.readFileSync(
    `${templateDirectoryPath}/${DISCLAIMER_TEMPLATE}`
  );
  schemasAndGenFiles.map(([schema, genFile]: [any, string]) => {
    // Write generated Python scripts
    const pkg = schema['package'];
    const pkgPath = pkg.replace(/\./g, '/');
    mkdirp.sync(`${OUT}/${SRC_DIRECTORY}/${pkgPath}`);
    const eventName = schema.name;
    fs.writeFileSync(
      `${OUT}/${SRC_DIRECTORY}/${pkgPath}/${eventName}.py`,
      disclaimer + genFile
    );

    const eventDescription = schema.description.replace(/\n/g, '');
    const event = {
      package: pkg,
      eventName: eventName,
      eventDescription: eventDescription,
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
}

if (!module.parent) {
  main();
}
