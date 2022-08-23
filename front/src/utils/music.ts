import axios from "axios";

const headers = {
  "Content-Type": "application/json",
  "Access-Control-Allow-Origin": "*",
};

export const next = async (player: string) =>
  await axios.post(
    `${process.env.REACT_APP_LOCAL_CLIENT_URL}/music/next`,
    null,
    {
      params: { player: player },
      headers,
    }
  );

export const getMetadata = async (player?: string) =>
  await axios.get(`${process.env.REACT_APP_LOCAL_CLIENT_URL}/music/metadata`, {
    params: {
      players: player,
    },
    headers,
  });

export const fetchPosision = async (player: string) =>
  await axios.get(`${process.env.REACT_APP_LOCAL_CLIENT_URL}/music/position`, {
    params: {
      player: player,
    },
  });

export const previousSong = async (player: string) =>
  await axios.post(
    `${process.env.REACT_APP_LOCAL_CLIENT_URL}/music/previous`,
    null,
    {
      params: { player: player },
    }
  );

export const tooglePlayer = async (player: string) =>
  await axios.post(
    `${process.env.REACT_APP_LOCAL_CLIENT_URL}/music/play_pause`,
    null,
    {
      params: { player: player },
    }
  );

export const timeSliderChange = async (value: number, player: string) =>
  await axios.post(
    `${process.env.REACT_APP_LOCAL_CLIENT_URL}/music/position`,
    null,
    {
      params: { player: player, value: value },
    }
  );

export const getPlayers = async () =>
  await axios.get(`${process.env.REACT_APP_LOCAL_CLIENT_URL}/music/players`);
