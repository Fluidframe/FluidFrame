/*
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import postcss from 'rollup-plugin-postcss';
import terser from '@rollup/plugin-terser';
import fs from 'fs';
import path from 'path';

// Parse command line arguments
const args = process.argv.slice(2);
const inputDir = args.find(arg => arg.startsWith('--input='))?.split('=')[1] || 'src';
const outputDir = args.find(arg => arg.startsWith('--output='))?.split('=')[1] || 'dist';

// Function to recursively get all .js files in a directory
function getJsFiles(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  list.forEach(file => {
    file = path.join(dir, file);
    const stat = fs.statSync(file);
    if (stat && stat.isDirectory()) {
      results = results.concat(getJsFiles(file));
    } else if (file.endsWith('.js')) {
      results.push(file);
    }
  });
  return results;
}

// Function to generate a valid JS identifier from a filename
function generateValidName(fileName) {
  return fileName
    .replace(/[^a-zA-Z0-9]/g, '_')
    .replace(/^[^a-zA-Z]/, '_');
}

// Get all .js files in input directory and its subdirectories
const scripts = getJsFiles(inputDir);

// Create a Rollup config for each script
const configs = scripts.map(script => {
  const relativePath = path.relative(inputDir, script);
  const dir = path.dirname(relativePath);
  const inputFileName = path.basename(script, '.js');
  const outputDirForFile = path.join(outputDir, dir);

  // Ensure the output directory exists
  if (!fs.existsSync(outputDirForFile)) {
    fs.mkdirSync(outputDirForFile, { recursive: true });
  }

  return {
    input: script,
    output: {
      file: path.join(outputDirForFile, `${inputFileName}.bundle.js`),
      format: 'iife',
      name: `Bundle${generateValidName(inputFileName)}`
    },
    plugins: [
      resolve({ browser: true }),
      commonjs(),
      postcss({ inject: true, minimize: true }),
      terser()
    ]
  };
});

export default configs;

*/

import { rollup } from 'rollup';
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import postcss from 'rollup-plugin-postcss';
import terser from '@rollup/plugin-terser';
import fs from 'fs';
import path from 'path';

// Parse command line arguments
const args = process.argv.slice(2);
const inputDir = args.find(arg => arg.startsWith('--input='))?.split('=')[1];
const outputDir = args.find(arg => arg.startsWith('--output='))?.split('=')[1];

if (!inputDir || !outputDir) {
  console.error('Input and output directories must be specified');
  process.exit(1);
}

console.log('Input directory:', inputDir);
console.log('Output directory:', outputDir);

// Function to recursively get all .js files in a directory
function getJsFiles(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  list.forEach(file => {
    file = path.join(dir, file);
    const stat = fs.statSync(file);
    if (stat && stat.isDirectory()) {
      results = results.concat(getJsFiles(file));
    } else if (file.endsWith('.js')) {
      results.push(file);
    }
  });
  return results;
}

// Function to generate a valid JS identifier from a filename
function generateValidName(fileName) {
  return fileName
    .replace(/[^a-zA-Z0-9]/g, '_')
    .replace(/^[^a-zA-Z]/, '_');
}

// Get all .js files in input directory and its subdirectories
const scripts = getJsFiles(inputDir);

// Create a Rollup config for each script
const configs = scripts.map(script => {
  const relativePath = path.relative(inputDir, script);
  const dir = path.dirname(relativePath);
  const inputFileName = path.basename(script, '.js');
  const outputDirForFile = path.join(outputDir, dir);

  // Ensure the output directory exists
  if (!fs.existsSync(outputDirForFile)) {
    fs.mkdirSync(outputDirForFile, { recursive: true });
  }

  return {
    input: script,
    output: {
      file: path.join(outputDirForFile, `${inputFileName}.bundle.js`),
      format: 'iife',
      name: `Bundle${generateValidName(inputFileName)}`
    },
    plugins: [
      resolve({ browser: true }),
      commonjs(),
      postcss({ inject: true, minimize: true }),
      terser()
    ]
  };
});

// Function to build all configs
async function build() {
  for (const config of configs) {
    try {
      const bundle = await rollup(config);
      await bundle.write(config.output);
      console.log(`Built: ${config.output.file}`);
    } catch (error) {
      console.error(`Error building ${config.input}:`, error);
    }
  }
}

build();