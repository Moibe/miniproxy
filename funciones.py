from gradio_client import Client, handle_file
import bridges
import time

#Función principal
def performa(input1):

    client = Client("Moibe/InstantID2")
    
    result = client.predict(
            face_image_path=handle_file('https://i.pinimg.com/236x/42/b4/6c/42b46c475fdc901cfccff9bfd4ae7da3.jpg'),
		    pose_image_path=handle_file('https://www.sexyshoes.com/cdn/shop/products/sleeveless-deep-cleavage-embroidered-mini-dress-fetish-dresses-noir-handmade-sexyshoescom.jpg'),
            prompt="anime school girl",
            negative_prompt="(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
            style_name="(No style)",
            num_steps=30,
            identitynet_strength_ratio=0.8,
            adapter_strength_ratio=0.8,
            canny_strength=0.4,
            depth_strength=0.4,
            controlnet_selection=["depth"],
            guidance_scale=5,
            seed=42,
            scheduler="EulerDiscreteScheduler",
            enable_LCM=False,
            enhance_face_region=True,
            api_name="/generate_image"
    )

    print("Éste es el resultado: ")
    print(result)      

    return result

if __name__ == "__main__":
    
    performa(1)