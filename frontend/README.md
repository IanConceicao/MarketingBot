# Frontend

## Installation

```
npm install
npm run validate
```

## Start Dev

```
npm run dev
```

## Start Production

Set `BACKEND_URL` environment variable to the production endpoint. Then run:

```
npm run build
```

## All Commands

```sh
npm run dev             # start development server
npm run start           # start development server
npm run validate        # run test,lint,build,typecheck concurrently
npm run test            # run jest
npm run lint            # run eslint
npm run lint:fix        # run eslint with --fix option
npm run typecheck       # run TypeScript compiler check
npm run build           # build production bundle to 'dist' directly
npm run prettier        # run prettier for json|yml|css|md|mdx files
npm run clean           # remove 'node_modules' 'yarn.lock' 'dist' completely
npm run serve           # launch server for production bundle in local
npm run remove:tailwind # remove TailwindCSS
```
