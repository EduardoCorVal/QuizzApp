import "./App.css";
import Register from "./pages/Register";
import Header from "./components/Header";
import Question from "./components/Question";
import Subtitle from "./components/Subtitle";
import Ejemplo from "./images/ejemplo.png"

function App() {
  return (
    <div className="App">
      <Header />
      <Question
        question="What is the capital of India?"
        image={Ejemplo}
        option1="Mumbai"
        option2="Delhi"
        option3="Kolkata"
        option4="Chennai"
        answer="Delhi"
      />
    </div>
  );
}

export default App;
