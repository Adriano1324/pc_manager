import { timeSliderChange } from "../../../utils/music";
import * as S from "./styles";

export const ProgressBar: React.FC<{
  position: number;
  duration: number;
  player: string;
}> = ({ position, duration, player }) => {
  return (
    <S.ProgressBarWrapper>
      <S.ProgressBar
        type="range"
        min={0}
        max={duration}
        value={position}
        step={1}
        onChange={(e) => timeSliderChange(Number(e.target.value), player)}
      />
    </S.ProgressBarWrapper>
  );
};
