import React, { useEffect, useState } from "react";
import { i18n } from "@lingui/core";
import { I18nProvider } from "@lingui/react";
import { en, pl } from "make-plural/plurals";
import Cookies from "universal-cookie";

import enMessages from "../../locales/en/messages";
import plMessages from "../../locales/pl/messages";
import { Locale } from "../../types/baseTypes";

import { LanguageProviderContext } from "./context";

i18n.loadLocaleData("en", { plurals: en });
i18n.loadLocaleData("pl", { plurals: pl });

i18n.load("en", enMessages.messages);
i18n.load("pl", plMessages.messages);

i18n.activate("en");

interface LanguageProviderProps {
  children: React.ReactNode;
}

export const LanguageProvider: React.FC<LanguageProviderProps> = ({
  children,
}) => {
  const cookies = new Cookies();
  const [language, setLanguage] = useState<Locale>(cookies.get("LOCALE"));

  useEffect(() => {
    cookies.set("LOCALE", language);
    i18n.activate(language);
  }, [language]); //eslint-disable-line react-hooks/exhaustive-deps
  // cookeis is not a dependency

  return (
    <LanguageProviderContext.Provider value={{ language, setLanguage }}>
      <I18nProvider i18n={i18n}>{children}</I18nProvider>
    </LanguageProviderContext.Provider>
  );
};
