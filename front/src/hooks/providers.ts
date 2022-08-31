import { useContext } from "react";
import { PlayerProviderContext, LanguageProviderContext, LightProviderContext } from "../providers";

export const usePlayerContext = () => useContext(PlayerProviderContext);
export const useLanguageContext = () => useContext(LanguageProviderContext);
export const useLightContext = () => useContext(LightProviderContext);
