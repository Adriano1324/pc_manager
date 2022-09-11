import { gql } from "@apollo/client";

export const PlayerListQuery = gql`
  query PlayerListQuery {
    listActualPlayers {
      name
    }
  }
`;

