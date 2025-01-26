const esbuild = require('esbuild');
const vuePlugin = require('esbuild-plugin-vue3');

esbuild.context({
  entryPoints: ['src/main.js'],
  bundle: true,
  outfile: 'dist/bundle.js',
  plugins: [vuePlugin()],
  sourcemap: true,
  define: {
    'process.env.NODE_ENV': '"development"',
  },
}).then(ctx => {
  // Start watching the files
  ctx.watch();
}).catch(() => process.exit(1));