# PC Manager Frontend

## Prerequisites

- nvm - [Installation guide](https://github.com/nvm-sh/nvm#installing-and-updating)
- yarn - [Installation guide](https://classic.yarnpkg.com/lang/en/docs/install/#debian-stable)

## Installing the frontend dependencies

Activate required node version:

    nvm use

If not installed run:

    nvm install
    nvm use

Install node dependencies

    yarn


## Commands

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `yarn locale`

Generates locale files used to generate translations. You need change manually locale files other than English to provide translations.

### `yarn locale:compile`

Compiles the locale files. Compiled files are used on page. Make sure to provide translations for all languages before executing this command.

### `yarn test`

Runs the test watcher in an interactive mode.

### `yarn build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!
