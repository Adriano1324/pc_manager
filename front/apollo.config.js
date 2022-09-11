require("dotenv").config();

module.exports = {
  name: "local-agent",
  client: {
    excludes: ["**/static/**/*"],
    service: {
      name: "local-agent",
      url: `http://${process.env.REACT_APP_LOCAL_AGENT_API_DOMAIN}/graphql/`,
    },
  },
};
