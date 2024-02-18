const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

const { spawn } = require("child_process");

// Example: Run a Python script that takes command line arguments
const pythonProcess2 = spawn("python", ["backend.py"]);
const pythonProcess1 = spawn("python", ["CreateOutput.py"]);

pythonProcess1.stdout.on("data", (data) => {
    console.log(data.toString());
    // Send 'data' to the client-side (browser) for display
});

pythonProcess2.stdout.on("data", (data) => {
    console.log(data.toString());
    // Send 'data' to the client-side (browser) for display
});
const executePythonScript = () => {
    exec('python CreateOutput.py', (error, stdout, stderr) => {
        if (error) {
            console.error(`Error executing Python script: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`Error executing Python script: ${stderr}`);
            return;
        }
        console.log('Python script executed successfully:', stdout);
    });
};
// Serve static files from the public directory
app.use(express.static('public'));

// Route to serve the index.html file
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
