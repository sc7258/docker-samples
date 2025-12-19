# Use an official Node.js runtime as a parent image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the application file into the container at /usr/src/app
COPY server.js .

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run server.js when the container launches
CMD ["node", "server.js"]
