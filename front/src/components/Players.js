import React, { useState, useEffect } from "react";
import LocalClient from "../axios/local_client";
import Player from "./Player";
const Players = () => {
  const [players, setPlayers] = useState([]);
  useEffect(() => {
    fetchPlayers();
  }, []);
  const fetchPlayers = () => {
    LocalClient.get("/music/metadata")
      .then((res) => {
        console.log(res);
        setPlayers(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };
  return (
    <div>
      {players.map((player) => (
        <div>
          <Player key={player.player} player={player.player} />
        </div>
      ))}
    </div>
  );
};

export default Players;
