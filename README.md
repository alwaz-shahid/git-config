<h1>Git Config Tool</h1>
    <p>This is a Python CLI tool to manage Git global user configuration.</p>

  <h2>Installation</h2>
    <ol>
        <li>Ensure you have Python and Git installed on your system.</li>
        <li>Clone or download the repository.</li>
        <li>Navigate to the repository directory.</li>
        <li>Run the script using Python:</li>
        <code>python main.py</code>
    </ol>

   <h2>Usage</h2>
    <p>Run the script with the following commmand:</p>
    <ul>
        <li><code>python main.py</code>: Set the Git global user configurations.</li>
    </ul>


  <h2>Contributing</h2>
    <p>Contributions are welcome! Feel free to open issues or submit pull requests.</p>

   <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p>

  <h1>Virtual Environment Setup Guide</h1>

 <p>To activate a virtual environment and install packages on different operating systems, follow these steps:</p>

 <h2>Create a Virtual Environment (if not already created)</h2>
    <p>If you haven't created a virtual environment yet, use the <code>venv</code> module, which comes bundled with Python 3.3 and later, to create one. Open your terminal or command prompt and navigate to your project directory. Then, run the following command:</p>

<pre><code>python -m venv venv</code></pre>

<p>This will create a new virtual environment named <code>venv</code> in your project directory.</p>

 <h2>Activate the Virtual Environment</h2>
    <p>Once you have created the virtual environment, you need to activate it. This will modify your terminal or command prompt to use the Python interpreter and packages from the virtual environment.</p>

<h3>On Windows</h3>
<pre><code>venv\Scripts\activate</code></pre>

 <h3>On Linux/Mac</h3>
    <pre><code>source venv/bin/activate</code></pre>

 <p>After activation, you will see <code>(venv)</code> at the beginning of your terminal or command prompt, indicating that the virtual environment is active.</p>

 <h3>Install packages from requirements.txt</h3>
    <pre><code> pip install -r requirements.txt</code></pre>
  <h2>Install Packages</h2>
    <p>With the virtual environment activated, you can now install packages using <code>pip</code>:</p>

 <pre><code>pip install package_name</code></pre>

  <p>Replace <code>package_name</code> with the name of the package you want to install. The package will be installed within the virtual environment, keeping it isolated from the global Python installation.</p>
 <h2>Deactivate the Virtual Environment</h2>
    <p>When you're done working on your project or want to switch back to the global Python environment, you can deactivate the virtual environment. Simply run:</p>

  <pre><code>deactivate</code></pre>

 <p>This will return your terminal or command prompt to the standard Python environment.</p>

