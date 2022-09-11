import { useQuery } from "@apollo/client";
import React, { useState, useEffect } from "react";
import { BrandIcon } from "../../components/BrandIcon";
import { PlayerListQuery } from "../../graphql/queries/player";
import { PlayerListQuery as PlayerListQueryType } from "../../graphql/__generated__/PlayerListQuery";
// import { getMetadata, getPlayers, tooglePlayer } from "../../utils/music";

import { Player } from "./components";
import {
  defaultPlayerContext,
  PlayerContext,
  PlayerProviderContext,
} from "./context";

interface PlayerProviderProps {
  children: React.ReactNode;
}

export const PlayerProvider: React.FC<PlayerProviderProps> = ({ children }) => {
  const [ctx, setCtx] = useState<PlayerContext>(defaultPlayerContext);
  const [players, setPlayers] = useState<string[]>([]);

  // const toggle = (isPlaying: boolean) => {
  //   tooglePlayer(ctx.player || "");
  //   setCtx({ ...ctx, isPlaying });
  // };

  // useEffect(() => {
  //   getPlayers().then((response) => setPlayers(response.data));
  //   setCtx({ ...ctx, player: players[0] });
  // }, []); // eslint-disable-line react-hooks/exhaustive-deps
  // // run only once when the component is mounted

  // useEffect(() => {
  //   const init = setInterval(
  //     () =>
  //       getMetadata(players[0]).then((response) => {
  //         setCtx({
  //           ...ctx,
  //           isPlaying: response.data[0].status === "Playing",
  //           trackInfo: {
  //             title: response.data[0].metadata.title,
  //             artist: response.data[0].metadata.albumArtist,
  //             thumbnail: response.data[0].metadata.artUrl,
  //             url: response.data[0].metadata.url,
  //             position: response.data[0].position,
  //             duration: response.data[0].metadata.length,
  //           },
  //         });
  //       }),
  //     1000
  //   );

  //   return () => clearInterval(init);
  // }, [players, ctx]);
  const { loading, error, data } = useQuery<PlayerListQueryType>(PlayerListQuery);
  return (
    <PlayerProviderContext.Provider value={{ ...ctx }}>
      {error && "Error"}
      {data?.listActualPlayers.map(
        (player) =>{
          console.log(player.name);
          return (
            player.name !== "no player found" && (
              <BrandIcon name={player.name} key={player.name}/>
            )
          );}
      )}
      {children}
      {!loading && ctx.player && <Player />}
    </PlayerProviderContext.Provider>
  );
};
