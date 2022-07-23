const loc = document.querySelector('.location');

function success(pos) {
    const crd = pos.coords;
    
    const lociq = `https://us1.locationiq.com/v1/reverse?key=pk.4f1c6e23668c6d93ef0c18fa30b60f6c&lat=${crd.latitude}&lon=${crd.longitude}&format=json`;
    fetch(lociq)
        .then(res => {
            return res.json();
        })
        .then(data => {
            loc.textContent=`${data.address.state},${data.address.city}, ${data.address.postcode} `;
        })
        .catch(()=>{loc.textContent='Unable to access your current location';
    });
}
 function error(err) {
    loc.textContent='Unable to access your current location';

}

navigator.geolocation.getCurrentPosition(success, error);



