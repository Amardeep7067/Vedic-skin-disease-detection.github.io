Parse.initialize(
    "7gAwbIlMNZu2K3A48k75uPwRGQPnL5CJ3QRMmTDg",
    "u3mxCA2KMeyu2Egd6v7Rek9QnRR5aKTGJLilMDCA"
  );

Parse.serverURL = 'https://pg-app-ugdod8udrehs2ez32vcv5kzl3c5881.scalabl.cloud/1/';



if(document.getElementById("red")){
    const URL = "https://teachablemachine.withgoogle.com/models/LILsZ-Czn/";

let model, webcam, newlabel, canvas, labelContainer, maxPredictions, camera_on = false, image_upload = false;
function useWebcam() {
    camera_on = !camera_on;

    if (camera_on) {
        init();
        document.getElementById("webcam").innerHTML = "Close Webcam";
    }
    else {
        stopWebcam();
        document.getElementById("webcam").innerHTML = "Start Webcam";
    }
}

async function stopWebcam() {
    await webcam.stop();
    document.getElementById("webcam-container").removeChild(webcam.canvas);
    labelContainer.removeChild(newlabel);
}



// Load the image model and setup the webcam
async function init() {

    const modelURL = URL + "model.json";
    const metadataURL = URL + "metadata.json";

    // load the model and metadata
    model = await tmImage.load(modelURL, metadataURL);
    maxPredictions = model.getTotalClasses();

    // Convenience function to setup a webcam
    const flip = true; // whether to flip the webcam
    webcam = new tmImage.Webcam(200, 200, flip); // width, height, flip
    await webcam.setup(); // request access to the webcam
    await webcam.play();
    window.requestAnimationFrame(loop);
    

    // append element to the DOM
    document.getElementById("webcam-container").appendChild(webcam.canvas);

    newlabel = document.createElement("div");
    labelContainer = document.getElementById("label-container");
    labelContainer.appendChild(newlabel);
}



async function loop() {
    webcam.update(); // update the webcam frame
    await predict(webcam.canvas);
    window.requestAnimationFrame(loop);
}

// run the image through the image model
async function predict(input) {
    // predict can take in an image, video or canvas html element
    const prediction = await model.predict(input);

    var highestVal = 0.00;
    var bestClass = "";
    result = document.getElementById("label-container");
    for (let i = 0; i < maxPredictions; i++) {
        var classPrediction = prediction[i].probability.toFixed(2);
        if (classPrediction > highestVal) {
            highestVal = classPrediction;
            bestClass = prediction[i].className;
        }
    }

  

    newlabel.innerHTML = bestClass;
}
}


if(document.getElementById("green")){
        // More API functions here:
			// https://github.com/googlecreativelab/teachablemachine-community/tree/master/libraries/image

			// the link to your model provided by Teachable Machine export panel
			const URL = "https://teachablemachine.withgoogle.com/models/LILsZ-Czn/";

			let model, labelContainer, maxPredictions;

			// Load the image model 
			async function init() {
				const modelURL = URL + 'model.json';
				const metadataURL = URL + 'metadata.json';

				// load the model and metadata
				model = await tmImage.load(modelURL, metadataURL);
				maxPredictions = model.getTotalClasses();

				labelContainer = document.getElementById('im-container');
				for (let i = 0; i < maxPredictions-6; i++) {
					// and class labels
					labelContainer.appendChild(document.createElement('div'));
				}
			}

			// async function predict() {
			// 	// predict can take in an image, video or canvas html element
			// 	var image = document.getElementById('imagePreview');
			// 	const prediction = await model.predict(image, false);
			// 	for (let i = 0; i < maxPredictions; i++) {
			// 		const classPrediction =
			// 			prediction[i].className + ': ' + prediction[i].probability.toFixed(2);
			// 		labelContainer.childNodes[i].innerHTML = classPrediction;
			// 	}
			// }

            async function predict() {
				// predict can take in an image, video or canvas html element
				var image = document.getElementById('imagePreview');
				const prediction = await model.predict(image, false);

                var highestVal = 0.00;
                var bestClass = "";
				for (let i = 0; i < maxPredictions; i++) {
					
                    var classPrediction = prediction[i].probability.toFixed(2);
                    if(classPrediction > highestVal){
                        highestVal = classPrediction;
                        bestClass = prediction[i].className;
                    }
					
				}
                labelContainer.innerHTML = bestClass;

			}
        
       

            function readURL(input) {
				if (input.files && input.files[0]) {
					var reader = new FileReader();
					reader.onload = function (e) {
						$('#imagePreview').attr('src', e.target.result);
						// $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
						$('#imagePreview').hide();
						$('#imagePreview').fadeIn(650);
					};
					reader.readAsDataURL(input.files[0]);
					init().then(() => {
						predict();
					});
				}
			}
			$('#imageUpload').change(function () {
				readURL(this);
			});

         
}

