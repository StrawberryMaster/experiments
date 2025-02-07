document.addEventListener('DOMContentLoaded', function () {
    const imageUpload = document.getElementById('imageUpload');
    const imagePreview = document.getElementById('imagePreview');
    const placeholderText = document.getElementById('placeholderText');
    let uploadedImage = null;
    let isDragging = false;
    let startX, startY, imgStartLeft, imgStartTop;

    imageUpload.addEventListener('change', function (event) {
        const file = event.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = function (e) {
            if (placeholderText) {
                placeholderText.remove();
            }
            if (uploadedImage) {
                uploadedImage.remove();
            }

            uploadedImage = document.createElement('img');
            uploadedImage.id = 'uploadedImage';
            uploadedImage.src = e.target.result;

            uploadedImage.onload = function () {
                const containerWidth = imagePreview.clientWidth;
                const containerHeight = imagePreview.clientHeight;
                const imgWidth = uploadedImage.naturalWidth;
                const imgHeight = uploadedImage.naturalHeight;

                const scale = Math.max(containerWidth / imgWidth, containerHeight / imgHeight);
                const displayWidth = imgWidth * scale;
                const displayHeight = imgHeight * scale;
                uploadedImage.style.width = displayWidth + 'px';
                uploadedImage.style.height = displayHeight + 'px';

                const left = (containerWidth - displayWidth) / 2;
                const top = (containerHeight - displayHeight) / 2;
                uploadedImage.style.left = left + 'px';
                uploadedImage.style.top = top + 'px';

                // Salva dimensões para aplicar limites durante o drag
                uploadedImage.dataset.displayWidth = displayWidth;
                uploadedImage.dataset.displayHeight = displayHeight;
                uploadedImage.dataset.containerWidth = containerWidth;
                uploadedImage.dataset.containerHeight = containerHeight;
            };

            imagePreview.appendChild(uploadedImage);

            uploadedImage.addEventListener('mousedown', function (e) {
                isDragging = true;
                startX = e.clientX;
                startY = e.clientY;
                imgStartLeft = parseInt(uploadedImage.style.left, 10);
                imgStartTop = parseInt(uploadedImage.style.top, 10);
                e.preventDefault();
            });
        };
        reader.readAsDataURL(file);
    });

    document.addEventListener('mousemove', function (e) {
        if (!isDragging || !uploadedImage) return;
        const dx = e.clientX - startX;
        const dy = e.clientY - startY;
        
        const containerWidth = parseFloat(uploadedImage.dataset.containerWidth);
        const containerHeight = parseFloat(uploadedImage.dataset.containerHeight);
        const displayWidth = parseFloat(uploadedImage.dataset.displayWidth);
        const displayHeight = parseFloat(uploadedImage.dataset.displayHeight);

        let newLeft = imgStartLeft + dx;
        let newTop = imgStartTop + dy;
        
        newLeft = Math.min(0, Math.max(newLeft, containerWidth - displayWidth));
        newTop = Math.min(0, Math.max(newTop, containerHeight - displayHeight));

        uploadedImage.style.left = newLeft + 'px';
        uploadedImage.style.top = newTop + 'px';
    });

    document.addEventListener('mouseup', function () {
        isDragging = false;
    });
});
