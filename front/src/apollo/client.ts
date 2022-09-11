import { ApolloClient, InMemoryCache } from "@apollo/client";

export const client = new ApolloClient({
  uri: `http://${
    process.env.REACT_APP_LOCAL_AGENT_API_DOMAIN
  }/graphql/`,
  cache: new InMemoryCache(),
});
