import { useRef, useState, useEffect } from 'react'
import './Dartboard.css'

const DARTBOARD_RADIUS = 75

function Dartboard() {
  const sections = [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5]
// const sections=[20, 1, 18]
  return (
    <>
        {sections.map((section, index) => {
            return <DartboardSection section={section} index={index}/>
        })}
    </>
  )
}

function DartboardSection(props){
    const {section, index} = props
    const canvasRef = useRef(null)

    const color = index % 2 === 0 ? 'black' : 'white'

    const draw = ctx => {
        ctx.fillStyle = color
        ctx.beginPath();
        ctx.arc(DARTBOARD_RADIUS, DARTBOARD_RADIUS, DARTBOARD_RADIUS,(Math.PI / 20)+ index/2 , -(Math.PI / 20)+ index/2 , true);
        ctx.lineTo(DARTBOARD_RADIUS, DARTBOARD_RADIUS);
        ctx.fill();

      }
      
      useEffect(() => {
        
        const canvas = canvasRef.current
        const context = canvas.getContext('2d')
        
        //Our draw come here
        draw(context)
      }, [draw])
    return (
        <canvas ref={canvasRef} className='dartboard--section-canvas'/>
    ) 

}

export default Dartboard