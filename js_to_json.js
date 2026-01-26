#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

function error(msg) {
  console.error(msg);
  process.exit(2);
}

const file = process.argv[2];
if (!file) error('Usage: node js_to_json.js <file.js>');
if (!fs.existsSync(file)) error('File not found: ' + file);

let src = fs.readFileSync(file, 'utf8');
let acorn;
try {
  acorn = require('acorn');
} catch (e) {
  console.error('Missing dependency: acorn. Install with: npm install acorn');
  process.exit(3);
}

try {
  const ast = acorn.parse(src, { ecmaVersion: 'latest', sourceType: 'module', ranges: true });
  const results = {};
  const { runInNewContext } = require('vm');

  for (const node of ast.body) {
    // var/let/const declarations
    if (node.type === 'VariableDeclaration') {
      for (const decl of node.declarations) {
        if (!decl.id || !decl.init) continue;
        const name = decl.id.name || (decl.id.type === 'Identifier' && decl.id.name) || null;
        if (!name) continue;
        const t = decl.init.type;
        if (t === 'ObjectExpression' || t === 'ArrayExpression') {
          const code = src.slice(decl.init.start, decl.init.end);
          try {
            const obj = runInNewContext('(' + code + ')');
            results[name] = obj;
          } catch (e) {
            // skip
          }
        }
      }
    }
    // assignments like window.var = {...}
    else if (
      node.type === 'ExpressionStatement' &&
      node.expression &&
      node.expression.type === 'AssignmentExpression'
    ) {
      const left = node.expression.left;
      const right = node.expression.right;
      let name = null;
      if (left.type === 'MemberExpression') {
        if (left.property && left.property.type === 'Identifier') name = left.property.name;
      } else if (left.type === 'Identifier') {
        name = left.name;
      }
      if (!name || !right) continue;
      if (right.type === 'ObjectExpression' || right.type === 'ArrayExpression') {
        const code = src.slice(right.start, right.end);
        try {
          const obj = runInNewContext('(' + code + ')');
          results[name] = obj;
        } catch (e) {}
      }
    }
  }

  // print JSON
  console.log(JSON.stringify(results, null, 2));
} catch (e) {
  console.error('Parse error: ' + e.message);
  process.exit(2);
}
