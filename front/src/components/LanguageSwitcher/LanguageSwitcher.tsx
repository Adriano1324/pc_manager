import React from "react";

import { useLanguageContext } from "../../hooks";

import * as S from "./styles";

export const LanguageSwitcher = () => {
  const { setLanguage } = useLanguageContext();
  return (
    <S.Wrapper>
      <S.Item onClick={() => setLanguage("en")}>English</S.Item>
      <span>&nbsp;/&nbsp;</span>
      <S.Item onClick={() => setLanguage("pl")}>Polski</S.Item>
    </S.Wrapper>
  );
};
