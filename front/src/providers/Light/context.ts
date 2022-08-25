import { createContext } from "react";

export interface Light {
  [key: string]: {
    ip: string;
    port: number;
    capabilities: {
      id: string;
      model: string;
      fw_ver: string;
      support: string;
      power: string;
      bright: string;
      color_mode: string;
      ct: string;
      rgb: string;
      hue: string;
      sat: string;
      name: string;
    };
  };
}

export type LightContext = {
  toggle: (ip: string) => void;

  bulbs: Light;
};

export const defaultLightContext: LightContext = {
  toggle: () => undefined,

  bulbs: {},
};

export const LightProviderContext =
  createContext<LightContext>(defaultLightContext);

LightProviderContext.displayName = "LightContext";
