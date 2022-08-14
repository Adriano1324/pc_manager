import styled from "styled-components";

export const PlayerWrapper = styled.div`
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 75px;
  padding: 10px 0;
  background-color: #000;
  color: #ccc;
`;

export const PlayerContainer = styled.div`
  width: 100%;
  max-width: 1200px;
  margin-inline: auto;
  display: flex;
  flex-direction: row;
  row-gap: 10px;
`;

export const TrackInfo = styled.div`
  position: relative;
  display: flex;
  flex-direction: row;
`;

export const ThumbnailWrapper = styled.div`
  width: 60px;
  height: 60px;
  border-radius: 5px;
  overflow: hidden;
`;
export const Thumbnail = styled.img`
  width: 60px;
  height: 60px;
`;

export const BasicInfo = styled.div`
  display: flex;
  flex-direction: column;
  padding: 0 6px;
`;

export const Title = styled.h4`
  color: #ccc;
  font-weight: 700;
  font-size: 1.2rem;
`;
export const Author = styled.h5`
  color: #aaa;
  font-weight: 400;
  font-size: 0.8rem;
`;

export const Controls = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 0 10px;
  width: 150px;
`;

export const ProgressBarWrapper = styled.div`
  display: block;
  width: 100%;
`;

export const ProgressBar = styled.input`
  width: 100%;
  height: 5px;
  border-radius: 5px;
  background-color: #333;
  border: none;
  outline: none;
  opacity: 0.7;
  transition: opacity 0.2s;

  &::-webkit-slider-thumb {
    appearance: none;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #fff;
    cursor: pointer;
  }
  &::-moz-range-thumb {
    width: 100%;
    height: 5px;
    background-color: #ccc;
    border-radius: 5px;
  }
  &:hover {
    cursor: pointer;
    opacity: 1;
  }
`;
