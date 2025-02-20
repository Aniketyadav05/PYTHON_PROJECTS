# Screen OCR Script

This Python script captures a screenshot of a specific region on the screen and applies Optical Character Recognition (OCR) to extract text from that region. It then searches for a specific pattern (in this case, the UID) and displays the extracted UID if found.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- Tesseract OCR (`pytesseract`)
- `notifypy`
- `pyautogui`

## Installation
- Close this repo and `cd` into it.
- Run `python -m venv env` to create a virtual environment named "env" (you can choose any name you want).
- Run `source env/bin/activate` to activate the virtual environment, replace env with your created virtual environment's name if different.
- You can install the required packages using the following command: `pip install -r requirements.txt`

## Usage

To run the script, execute the following command:

`python main.py <mode>`

Replace `<mode>` with either `test` or `capture`. 
- `test` mode uses a predefined test image (`test.jpeg`),
- `capture` mode captures a screenshot of the screen in real-time.
- `live` mode captured every 1 second in realtime

## Gotchas
Please place the input on the bottom right corner, with more than 70% width and height of the window to be able gather the text properly; otherwise results might be inaccurate.

<svg version="1.2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="600" >
	<title>New Project</title>
	<defs>
		<image  width="1920" height="1080" id="img1" href="data:image/png;base64,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"/>
	</defs>
	<style>
		tspan { white-space:pre } 
		.t0 { font-size: 83px;fill: #840606;font-weight: 400;font-family: "DejaVuSans", "DejaVu Sans" } 
		.t1 { font-size: 83px;fill: #ffffff;font-weight: 400;font-family: "DejaVuSans", "DejaVu Sans" } 
	</style>
	<use id="Background" href="#img1" x="0" y="0"/>
	<text id="DESKTOP" style="transform: matrix(1,0,0,1,77,73)" >
		<tspan x="0" y="63.1" class="t0">D</tspan><tspan  y="63.1" class="t0">E</tspan><tspan  y="63.1" class="t0">S</tspan><tspan  y="63.1" class="t0">K</tspan><tspan  y="63.1" class="t0">T</tspan><tspan  y="63.1" class="t0">O</tspan><tspan  y="63.1" class="t0">P</tspan><tspan  y="63.1" class="t0">
</tspan>
	</text>
	<text id="Area to be observed" style="transform: matrix(1,0,0,1,541.613,386.695)" >
		<tspan x="0" y="0" class="t1">A</tspan><tspan  y="0" class="t1">r</tspan><tspan  y="0" class="t1">e</tspan><tspan  y="0" class="t1">a</tspan><tspan  y="0" class="t1"> </tspan><tspan  y="0" class="t1">t</tspan><tspan  y="0" class="t1">o</tspan><tspan  y="0" class="t1"> </tspan><tspan  y="0" class="t1">b</tspan><tspan  y="0" class="t1">e</tspan><tspan  y="0" class="t1"> </tspan><tspan  y="0" class="t1">o</tspan><tspan  y="0" class="t1">b</tspan><tspan  y="0" class="t1">s</tspan><tspan  y="0" class="t1">e</tspan><tspan  y="0" class="t1">r</tspan><tspan  y="0" class="t1">v</tspan><tspan  y="0" class="t1">e</tspan><tspan  y="0" class="t1">d</tspan><tspan  y="0" class="t1">
</tspan>
	</text>
</svg>

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
