import { createContext } from "react";
import { Locale } from "../../types/baseTypes";

type LanguageContext = {
  language: Locale;
  setLanguage: (language: Locale) => void;
};

const defaultLanguageContext: LanguageContext = {
  language: "en",
  setLanguage: () => undefined,
};

export const LanguageProviderContext = createContext<LanguageContext>(
  defaultLanguageContext
);

LanguageProviderContext.displayName = "LanguageContext";
