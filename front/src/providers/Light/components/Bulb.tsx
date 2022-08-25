import React from "react";
import * as S from "./styles";
import { useLightContext } from "../../../hooks";
import LightbulbIcon from "@mui/icons-material/Lightbulb";
export const Bulb: React.FC<{
  ip: string;
}> = ({ ip }) => {
  const { bulbs, toggle } = useLightContext();
  return (
    <S.BulbContainer>
      <LightbulbIcon
        fontSize="inherit"
        color={bulbs[ip].capabilities.power === "on" ? "success" : "inherit"}
        onClick={() => toggle(ip || "")}
      />
    </S.BulbContainer>
  );
};
