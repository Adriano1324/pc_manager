import { Trans } from "@lingui/macro";
import React from "react";
import { LanguageSwitcher } from "./components";

function App() {
  return (
    <>
      <LanguageSwitcher />
      <div></div>
      <Trans>language provider test</Trans>
    </>
  );
}

export default App;
