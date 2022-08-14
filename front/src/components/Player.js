import React, { useState, useEffect } from "react";
import Slider from "@react-native-community/slider";
import LocalClient from "../axios/local_client";
import playNextMusic from "../functions/music_stering";
const Player = ({ player }) => {
  const [data, setData] = useState([]);
  const [position, setPosition] = useState([]);
  var previous_position = 0;
  function set_states(data) {
    setData(data);
    setPosition(data.position);
  }
  useEffect(() => {
    fetchMetadata();

    const interval = setInterval(() => {
      fetchPosision();
    }, 3000);

    return () => clearInterval(interval);
    // eslint-disable-next-line
  }, []);
  const fetchMetadata = () => {
    LocalClient.get("/music/metadata", {
      params: {
        players: player,
      },
    })
      .then((res) => {
        set_states(res.data[0]);
      })
      .catch((err) => {
        console.log(err);
      });
  };
  function fetchPosision() {
    LocalClient.get("/music/position", {
      params: {
        player: player,
      },
    })
      .then((res) => {
        setPosition(res.data);
        if (previous_position > res.data) {
          fetchMetadata();
        }
        previous_position = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  }
  function nextSong() {
    var res = playNextMusic(player)
    console.log(res)
    set_states(res)

  }
  function previousSong() {
    LocalClient.post("music/previous", null, {
      params: { player: player },
    })
      .then((res) => {
        set_states(res.data[0]);
      })
      .catch((err) => console.log(err));
  }
  function tooglePlayer() {
    LocalClient.post("music/play_pause", null, {
      params: { player: player },
    })
      .then((res) => {
        set_states(res.data[0]);
      })
      .catch((err) => console.log(err));
  }
  function timeSliderChange(value) {
    LocalClient.post("music/position", null, {
      params: { player: player, operation: value },
    })
      .then((res) => {
        set_states(res.data[0]);
      })
      .catch((err) => console.log(err));
  }

  return (
    <div>
      {data.metadata && (
        <div>
          {data.player}
          <br />
          {data.metadata.title}
          <br />
          <button onClick={previousSong}>previous</button>
          <button onClick={tooglePlayer}>
            {data.status === "Playing" ? "pause" : "play"}
          </button>
          <button onClick={nextSong}>next</button>

          <br />

          <button onClick={(e) => timeSliderChange("10-")}>&#60;&#60;</button>
          <button onClick={(e) => timeSliderChange("5-")}>&#60;</button>
          <Slider
            step={1}
            minimumValue={0}
            maximumValue={data.metadata.length ? data.metadata.length : 0}
            value={position}
            onSlidingComplete={timeSliderChange}
          />
          <button onClick={(e) => timeSliderChange("5+")}>&#62;</button>
          <button onClick={(e) => timeSliderChange("10+")}>&#62;&#62;</button>
        </div>
      )}
    </div>
  );
};

export default Player;
