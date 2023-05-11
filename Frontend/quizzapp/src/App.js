import { createContext, useState } from "react";
import AppContext from "./components/AppContext";
/* Main Style */
import "./App.css";

/* Pages */
import Register from "./pages/Register";
import Questions from "./pages/Questions";

export const UserContext = createContext();

function App() {
  const [page, setPage] = useState(0);
  const pages = [<Register page={page} setPage={setPage}/>, <Questions/>];

  return (
    <div className="App">
      <AppContext>
        {pages[page]}
      </AppContext>
    </div>
  );
}

export default App;
