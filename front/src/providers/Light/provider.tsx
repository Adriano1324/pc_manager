import React, { useState, useEffect } from "react";
import { getLights } from "../../utils/light";
import { toogleLight } from "../../utils/light";
import * as S from "./components/styles";

import { Bulb } from "./components";
import {
  Light,
  defaultLightContext,
  LightContext,
  LightProviderContext,
} from "./context";

interface LightProviderProps {
  children: React.ReactNode;
}

export const LightProvider: React.FC<LightProviderProps> = ({ children }) => {
  const [ctx, setCtx] = useState<LightContext>(defaultLightContext);
  const [lights, setLights] = useState<Light>({});

  const toggle = (ip: string) => {
    let bulbs = ctx.bulbs;
    toogleLight(ip, bulbs[ip].capabilities.power || "");
    bulbs[ip].capabilities.power === "on"
      ? (bulbs[ip].capabilities.power = "off")
      : (bulbs[ip].capabilities.power = "on");
    setCtx({ ...ctx, bulbs: bulbs });
  };

  // run only once when the component is mounted
  useEffect(() => {
    const init = setInterval(
      () =>
        getLights().then((response) =>
          setCtx({ ...ctx, bulbs: response.data })
        ),
      3000
    );

    return () => clearInterval(init);
  }, [ctx]);
  return (
    <LightProviderContext.Provider value={{ ...ctx, toggle }}>
      <S.BulbsWrapper>
        {Object.entries(ctx.bulbs).map(([key, value]) => (
          <Bulb ip={key} />
        ))}
      </S.BulbsWrapper>
    </LightProviderContext.Provider>
  );
};
