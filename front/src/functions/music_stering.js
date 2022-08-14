import LocalClient from "../axios/local_client";

function playNextMusic(player){
    LocalClient.post("music/next", null, {
        params: { player: player },
      })
        .then((res) => {
          return res.data[0];
        })
        .catch((err) => console.log(err));
}

export default playNextMusic