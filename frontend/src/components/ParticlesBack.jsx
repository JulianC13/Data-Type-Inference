import { useEffect, useMemo, useState } from "react";
import Particles, { initParticlesEngine } from "@tsparticles/react";
import { loadSlim } from "@tsparticles/slim"; // if you are going to use `loadSlim`, install the "@tsparticles/slim" package too.

function ParticlesBack(){   
   const [init, setInit] = useState(false);
   // this should be run only once per application lifetime
   useEffect(() => {
     initParticlesEngine(async (engine) => {
       await loadSlim(engine);
     }).then(() => {
       setInit(true);
     });
   }, []);
   
   const particlesLoaded = (container) => {
    //  console.log(container);
   };
   
   const options = useMemo(
     () => ({
       background: {
         color: {
           value: "#424244",
         },
       },
       fpsLimit: 120,
       interactivity: {
         events: {
           onClick: {
             enable: true,
             mode: "push",
           },
           onHover: {
             enable: true,
             mode: "repulse",
           },
         },
         modes: {
           push: {
             quantity: 4,
           },
           repulse: {
             distance: 200,
             duration: 0.4,
           },
         },
       },
       particles: {
         color: {
           value: "#ffffff",
         },
         links: {
           color: "#ffffff",
           distance: 150,
           enable: true,
           opacity: 0.5,
           width: 1,
         },
         move: {
           direction: "none",
           enable: true,
           outModes: {
             default: "bounce",
           },
           random: false,
           speed: 6,
           straight: false,
         },
         number: {
           density: {
             enable: true,
           },
           value: 80,
         },
         opacity: {
           value: 0.5,
         },
         shape: {
           type: "circle",
         },
         size: {
           value: { min: 1, max: 5 },
         },
       },
       detectRetina: true,
     }),
     [],
   );

    if (init) {
        return (
        <Particles
            id="tsparticles"
            particlesLoaded={particlesLoaded}
            options={options}/>
        );
    }
    return <></>;
}

export default ParticlesBack