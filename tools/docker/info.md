# What is Docker
Docker allows you to package applications with infrastructure
Get to version control your architecture
Good for highly distributed and higly available
Containers run anywhere that runs Docker
Simplifies Ops Jobs significantly

# Docker vs Vagrant
Docker cuts out alot of the pain associated with software architecture
Docker is lightweight
Doesnt require overhead of a guest OS

## Terms
* Container 
 * Running instance of your app and its complete software stack. The thing you build on your computer is not a computer, the program you run is the container
 * You might have many identical containers running
 * Often runs one process
* Image
 * Compiled distributable version of your app and its stack
 * Images are built from dockerfiles
 * you can start many containers from the same image
 * Significant Hard Drive Space Cost
* Layer
 * Docker uses a layering sustem to optimize storage
 * Each line in your dockerfile is a layer
 * Many alyers make up an image
 * Images can share layers
* Dockerfile
 * Plain textfile that should live in the root of our project
 * Describes how to build image
 * Installs software packages, configures runtimes, 
* Registry
 * A server that stores images
 * Provides organiazation and authentication
 * Facilities sharing prebuilt images, Dockerhub
* The Docker Binary
 * cli client and the server are both docker, 
 * written in Go
 * speaks via http to each other
 *
## How containers run
Docker daemon runs as root and starts containers
Containers are basically stateless, be carefully about writing files to a specific container
Can be exposed to real local storage if you need to
Outsource persistence

# Running the doctor daemon
unless you are running linux you need a VM
Use Docker for Max. Fast startup
Dont use ubuntu use CoreOs

