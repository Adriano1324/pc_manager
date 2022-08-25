import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import { LanguageProvider } from "./providers/Language";
import { PlayerProvider, LightProvider } from "./providers";

const root = ReactDOM.createRoot(
  document.getElementById("PC_MANAGER") as HTMLElement
);
root.render(
  <React.StrictMode>
    <LanguageProvider>
      <LightProvider> 
        <PlayerProvider>
          <App />
        </PlayerProvider>
      </LightProvider>
    </LanguageProvider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
