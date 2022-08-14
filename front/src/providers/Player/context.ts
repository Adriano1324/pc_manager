import { createContext } from "react";

export type PlayerContext = {
  next: (player: string) => void;
  previous: () => void;
  play: () => void;
  pause: () => void;
  toggle: (isPlaying: boolean) => void;
  stop: () => void;
  setVolume: (volume: number) => void;
  setPosition: (position: number) => void;
  open: (url: string) => void;
  loop: (isInLoop: boolean) => void;
  shuffle: (shuffleMode: boolean) => void;

  trackInfo: {
    url: string;
    thumbnail: string;
    title: string;
    artist: string;
    position: number;
    duration: number;
  };

  isPlaying: boolean;
  isLoop: boolean;
  isShuffle: boolean;
  volume: number;
  player: string | null;
};

export const defaultPlayerContext: PlayerContext = {
  next: () => undefined,
  previous: () => undefined,
  play: () => undefined,
  pause: () => undefined,
  toggle: () => undefined,
  stop: () => undefined,
  setVolume: () => undefined,
  setPosition: () => undefined,
  open: () => undefined,
  loop: () => undefined,
  shuffle: () => undefined,

  trackInfo: {
    url: "",
    thumbnail: "",
    title: "",
    artist: "",
    position: 0,
    duration: 0,
  },

  isPlaying: false,
  isLoop: false,
  isShuffle: false,
  volume: 0.5,
  player: null,
};

export const PlayerProviderContext =
  createContext<PlayerContext>(defaultPlayerContext);

PlayerProviderContext.displayName = "PlayerContext";
