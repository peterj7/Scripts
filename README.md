<h1>Scripts</h1>
<h3>Scripts for automating tasks (Python)</h3>
<br>
<p>*Requirements:</p>
<ol>
	<li><a href = "https://www.python.org/downloads/">Python</a> download</li>
	<ul>
		<li>set environment variables and make sure python is in PATH</li>
	</ul>
	<li><a href = "http://selenium-python.readthedocs.io/installation.html">Selenium</a> installaton</li>
	<li><a href = "https://sites.google.com/a/chromium.org/chromedriver/getting-started">Chromedriver</a> installation (if Google Chrome is desired web browser)</li>
	<li><a href  = "http://docs.python-requests.org/en/master/user/install/#install">Requests</a> installation (for some scripts)</li>
</ol>

<h3>Content</h3>
<ul>
	<li>AEM</li>
	<ul>
		<li>AEM Activate v1.0.py</li>
		<ul>
			<li>Input: 1 URL + multiple country codes</li>
			<li>Output: page of URL activated for each country code</li>
			<li>Description: automates the activation process of a desired page in AEM author for the desired countries</li>
		</ul>
		<li>AEM Activate v1.1.py</li>
		<ul>
			<li>Modified v1.0 to allow user to input url for external or AEM and converts to AEM</li>
		</ul>
		<li>AEM Activate v1.2.py</li>
		<ul>
			<li>Modified v1.1 to allow multiple URLs</li>
			<li>Input: multiple URLs + multiple country codes</li>
			<li>Output: pages of URL list activated for each country code</li>
		</ul>
		<li>AEM Activate v1.3.py</li>
		<ul>
			<li>Modified v1.2 to pull login credentials, desired URLs, and desired country codes from .txt files</li>
		</ul>
		<li>URL Opener v1.0.py</li>
		<ul>
			<li>Input: URL + multiple country codes</li>
			<li>Output: urls are opened in one web browser window</li>
			<li>Description: automates opening the same page across different countries in aem or externally</li>
		</ul>
		<li>URL Opener v1.1.py</li>
		<ul>
			<li>Modified v1.0 to allow multiple URLs</li>
		</ul>
		<li>URL Opener v1.2.py</li>
		<ul>
			<li>Modified v1.1 to allow preview mode based on user input and pull login credentials, desired URLs, and desired country codes from .txt files</li>
		</ul>
		<li>Find All Links v1.0</li>
		<ul>
			<li>Input: 1 URL</li>
			<li>Output: list of every link on that web page</li>
			<li>Description: automates listing every web address that the input web page links to</li>
		</ul>
	</ul>
	<li>Bookmarks</li>
	<li>(url, unique identifiers, country codes not provided)</li>
	<ul>
		<li>countrySwitch.js</li>
		<ul>
			<li>Description: locates the country code and switches to desired country code. AEM compatible</li>
		</ul>
		<li>alternativeCountrySwitch.js</li>
		<ul>
			<li>Description: locates the country code through specific identifiers. AEM compatible</li>
		</ul>
		<li>leadPage.js</li>
		<ul>
			<li>Description: navigates you to thanks or watch page, depending on url content. AEM compatible</li>
		</ul>
	</ul>
</ul>
