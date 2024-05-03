import "./App.css";
import { useState, useEffect } from "react";
import spin from "./images/spin.gif";
import lens from "./images/lens.png";
import StOlafLogo from "./images/StOlafPng.png";
import axios from 'axios';

const apiUri = "http://localhost:8000/predict"

function App() {
  const [prompt, updatePrompt] = useState<string>("");
  const [loading, setLoading] = useState(false);
  const [answer, setAnswer] = useState<string>("");

  
  /*
  const sendPrompt = async (event:any) => {
    if (event.key !== "Enter") {
      return;
    }
    try {
      setLoading(true);

      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
      };
      

      //This Line 'asks' the bot at /api/ask what to do with the given input
      //Change this line when we are ready for that
      const res = await fetch("/api/ask", requestOptions);
      if (!res.ok) {
        throw new Error("Something went wrong");
      }
  
      const { message } = await res.json();
      setAnswer(message);
    } catch (err) {
      console.error(err, "Caught Error");
    } finally {
      setLoading(false);
    }
  }
  */
  const sendPrompt = async (event:any) => {
    if (event.key !== "Enter") {
      return;
    }
    try {
      setLoading(true);
      setAnswer("")

      const response = await axios.post(
        apiUri, {
          "prompt": prompt
        }
      )

      const responseString = response.data;

      setAnswer(responseString);
    }
    catch (err) {
    console.error(err, "Caught Error");
    } finally {
    setLoading(false);
    }
  }

  useEffect(() => {
    if (prompt != null && prompt.trim() === "") {
      setAnswer("");
    }
  }, [prompt]);

  return (
    
    <div className="main">
      <div style={{ display: 'flex', alignItems: 'center', backgroundColor: 'lightgrey' }}>
        
        <a href='https://wp.stolaf.edu/'>
          <img src={StOlafLogo} alt="St Olaf Logo" style={{height: '70px', width: '230px'}}></img>
        </a>
        <div style={{height:'70px', width: '50px'}}></div>
        <h1> 
            Angora CS Chatbot
        </h1>
      </div>
      <div className="app">
        <div className="app-container">
          <div className="spotlight__wrapper">
          <input
              type="text"
              className="spotlight__input"
              placeholder="Ask me anything..."
              style={{
                backgroundImage: loading ? `url(${spin})` : `url(${lens})`,
              }}
              onChange={(e) => updatePrompt(e.target.value)}
              onKeyDown={(e) => sendPrompt(e)}
            />
            <div className="spotlight__answer">
              {answer && <p>{answer}</p>}
            </div>
          </div>
        </div>
      </div>
      <footer className="footer">
        For more resources:&nbsp;
        <a href='https://sites.google.com/stolaf.edu/cs-student-resources/home'>CS Student Resources</a>
      </footer>
    </div>
  );
}

export default App;
