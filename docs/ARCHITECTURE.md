# Architecture

Workload API → tenant admission → bounded scheduler → dedicated process pipe → validated handler → result. Optional WebAssembly module is a separate execution backend helper.
