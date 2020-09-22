#!/usr/bin/env node

import { Interface } from "readline";

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
const PY_FILENAME = 'events.py';
const INIT_PY_TEMPLATE = 'init_py.squirrelly';
const README_TEMPLATE = 'README.squirrelly';
const SETUP_PY_TEMPLATE = 'setup_py.squirrelly';
const VERSION = '0.0.1';

interface Event {
  package: string;
  eventName: string;
  eventDescription: string;
};

async function main() {
  if (!IN) console.error('Error in config: `IN` not set');
  if (!OUT) console.error('Error in config: `OUT` not set');
  if (!IN || !OUT) return;
  if (IN.endsWith('/')) IN = IN.substring(0, IN.length - 1);
  if (OUT.endsWith('/')) OUT = OUT.substring(0, OUT.length - 1);

  const templateDirectoryPath = `${__dirname}/../../${TEMPLATE_DIRECTORY}`;

  const schemasAndGenFiles = await qt.getJSONSchemasAndGenFiles(IN, LANGUAGE);
  const allEvents: Event[] = [];
  schemasAndGenFiles.map(([schema, genFile]: [any, string]) => {
    // Write generated Python scripts
    const pkg = schema['$id'];
    const pkgPath = pkg.replace(/\./g, '/');
    mkdirp.sync(`${OUT}/${SRC_DIRECTORY}/${pkgPath}`);
    fs.writeFileSync(
      `${OUT}/${SRC_DIRECTORY}/${pkgPath}/${PY_FILENAME}`,
      genFile
    );

    const pkgEvents: string[] = [];
    Object.keys(schema.properties).map((eventName: string) => {
      const eventDescription = schema.properties[eventName].description;
      pkgEvents.push(eventName);
      allEvents.push({
        package: pkg,
        eventName: eventName,
        eventDescription: eventDescription,
      });
    });

    // Write __init__.py scripts
    const initPySqrlTmpl = fs.readFileSync(
      `${templateDirectoryPath}/${INIT_PY_TEMPLATE}`
    );
    const initPy = sqrl.render(String(initPySqrlTmpl), {
      pkgEvents: pkgEvents,
    });
    fs.writeFileSync(`${OUT}/${SRC_DIRECTORY}/${pkgPath}/__init__.py`, initPy);
  });

  // Write the README.md file
  const readMeSqrlTmpl = fs.readFileSync(
    `${templateDirectoryPath}/${README_TEMPLATE}`
  );
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
