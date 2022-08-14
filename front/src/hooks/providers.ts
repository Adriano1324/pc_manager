import { useContext } from "react";
import { PlayerProviderContext, LanguageProviderContext } from "../providers";

export const usePlayerContext = () => useContext(PlayerProviderContext);
export const useLanguageContext = () => useContext(LanguageProviderContext);
