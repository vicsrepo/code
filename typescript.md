# TypeScript

[TypeScript](https://www.typescriptlang.org/) is a typed superset of JavaScript that compiles to JavaScript. Parcel supports TypeScript out of the box without any additional configuration.

### Transpilation

Parcel automatically transpiles TypeScript whenever you use a `.ts` or `.tsx` file. In addition to stripping the types to convert TypeScript to JavaScript, Parcel also compiles modern language features like classes and async await as necessary, according to your browser targets. It also transpiles JSX automatically. See the Transpilation section of the JavaScript docs for more details.

A `tsconfig.json` file can be used to configure some aspects of the transpilation. Currently, JSX options are supported, as well as the `experimentalDecorators` and `useDefineForClassFields` options. See the [TSConfig reference](https://www.typescriptlang.org/tsconfig) for details.

#### `isolatedModules`

Because Parcel processes each file individually, it implicitly enables the [`isolatedModules`](https://www.typescriptlang.org/tsconfig#isolatedModules) option. This means that some TypeScript features like `const enum` that require cross-file type information to compile will not work. To be warned about usages of these features in your IDE and during type checking, you should enable this option in your `tsconfig.json`.

#### TSC

[TSC](https://www.typescriptlang.org/docs/handbook/compiler-options.html) is the official TypeScript compiler from Microsoft. While Parcel’s default transpiler for TypeScript is much faster than TSC, you may need to use TSC if you are using some configuration in `tsconfig.json` that Parcel doesn't support. In these cases, you can use the `@parcel/transformer-typescript-tsc` plugin by adding it to your `.parcelrc`.

Even when using TSC, Parcel still processes each TypeScript file individually, so the note about `isolatedModules` still applies. In addition, some resolution features such as `paths` are not currently supported by Parcel. The TSC transformer also does not perform any type checking ([see below](broken-reference)).

#### Babel

You can also choose to use Babel to compile TypeScript. If a Babel config containing `@babel/preset-typescript` is found, Parcel will use it to compile `.ts` and `.tsx` files. Note that this has the same [caveats](https://babeljs.io/docs/en/babel-plugin-transform-typescript#caveats) about isolated modules as above. See Babel in the JavaScript docs for more details.

### Resolution

Parcel does not currently support the `baseUrl` or `paths` options in `tsconfig.json`, which are TypeScript specific resolution extensions. Instead, you may be able to use Parcel's tilde or absolute specifiers to accomplish a similar goal. See Configuring other tools in the dependency resolution docs for information about how to configure TypeScript to support these.

### Generating typings

When building a library, Parcel can extract the types from your entry point and generate a `.d.ts` file. Use the `types` field in `package.json` alongside a target such as `main` or `module` to enable this.

See Building a library with Parcel for more details.

### Type checking

By default, Parcel does not perform any type checking. The recommended way to type check is by using an editor with TypeScript support (such as VSCode), and using `tsc` to type check your code in CI. You can configure this using npm scripts to run alongside your build, tests, and linting.

#### Experimental validator plugin

The `@parcel/validator-typescript` plugin is an experimental way to type check within your Parcel build. It runs in the background after bundles are generated. Make sure the `include` option in `tsconfig.json` includes all of your source files.
