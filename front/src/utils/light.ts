import localAgent from "../axios/localAgent";

export const toogleLight = async (ip: string, state: string) => {
  if (state === "on")
    await localAgent.post("light/turn_off", null, {
      params: { ips: ip },
    });
  else
    await localAgent.post("light/turn_on", null, {
      params: { ips: ip },
    });
};

export const getLights = async () => await localAgent.get("light");
