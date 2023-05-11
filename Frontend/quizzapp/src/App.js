import { createContext, useState } from "react";
import AppContext from "./components/AppContext";
/* Main Style */
import "./App.css";

/* Pages */
import Register from "./pages/Register";
import Questions from "./pages/Questions";
import FinalScore from "./pages/FinalScore";

export const UserContext = createContext();

function App() {
  const [page, setPage] = useState(0);
  const pages = [<Register page={page} setPage={setPage}/>, <Questions page={page} setPage={setPage}/>, <FinalScore page={page} setPage={setPage}/>];

  return (
    <div className="App">
      <AppContext>
        {pages[page]}
      </AppContext>
    </div>
  );
}

export default App;
