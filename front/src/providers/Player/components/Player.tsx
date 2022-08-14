import PauseIcon from "@material-ui/icons/Pause";
import PlayArrowIcon from "@material-ui/icons/PlayArrow";
import SkipNextIcon from "@material-ui/icons/SkipNext";
import SkipPreviousIcon from "@material-ui/icons/SkipPrevious";
import { usePlayerContext } from "../../../hooks";

import { next, previousSong } from "../../../utils/music";
import { ProgressBar } from "./ProgressBar";
import * as S from "./styles";

export const Player: React.FC<{}> = () => {
  const { isPlaying, trackInfo, toggle, player } = usePlayerContext();

  return (
    <S.PlayerWrapper>
      <S.PlayerContainer>
        <S.ThumbnailWrapper>
          <S.Thumbnail
            src={trackInfo.thumbnail}
            alt={`${trackInfo.title} - ${trackInfo.artist}`}
          />
        </S.ThumbnailWrapper>
        <S.BasicInfo>
          <S.Title>{trackInfo.title}</S.Title>
          <S.Author>{trackInfo.artist}</S.Author>
        </S.BasicInfo>
        <SkipPreviousIcon onClick={() => previousSong(player ?? "")} />
        {isPlaying ? (
          <PauseIcon onClick={() => toggle(!isPlaying)} />
        ) : (
          <PlayArrowIcon onClick={() => toggle(!isPlaying)} />
        )}
        <SkipNextIcon onClick={() => next(player ?? "")} />
        <ProgressBar
          position={trackInfo.position}
          duration={trackInfo.duration}
          player={player ?? ""}
        />
      </S.PlayerContainer>
    </S.PlayerWrapper>
  );
};
