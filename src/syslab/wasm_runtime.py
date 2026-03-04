"""Optional actual WebAssembly execution. No WASI or host imports are provided."""
def add(wat,a,b,fuel=10000):
    import wasmtime
    if fuel<1:raise ValueError('positive fuel required')
    config=wasmtime.Config();config.consume_fuel=True;engine=wasmtime.Engine(config);store=wasmtime.Store(engine)
    store.set_fuel(fuel);store.set_limits(memory_size=65536,instances=1,memories=1,table_elements=0)
    module=wasmtime.Module(engine,wasmtime.wat2wasm(wat))
    if list(module.imports):raise ValueError('host imports not allowed')
    instance=wasmtime.Instance(store,module,[]);return instance.exports(store)['add'](store,a,b)
