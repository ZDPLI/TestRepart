# Setup and Installation

1. Install the required Python packages:
```bash
pip install -r requirements.txt
```

2. Download the Lingshu model repository and place it in a `models/` directory.
   The directory should contain the GGUF files (`Lingshu-7B.Q8_0.gguf` and
   `Lingshu-7B.mmproj-f16.gguf`) as well as the accompanying configuration files.
   Alternatively set the environment variable `LINGSHU_MODEL_DIR` to that
   directory.

3. (Optional) Verify GPU availability:
```bash
python gpu_support/check_gpu.py
```

4. Start the Flask backend:
```bash
python backend/app.py
```

5. Launch the Gradio web interface (provides multimodal chat capabilities):
```bash
python webui.py
```

The frontend HTML client can be opened directly in a browser from `frontend/index.html`.
