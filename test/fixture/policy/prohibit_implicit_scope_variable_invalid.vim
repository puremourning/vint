" Prohibit implicit scope variables
let explicit_global_var = 101

redir => output
redir END

" Prohibit implicit builtin variables
let count = 110

function! ImplicitGlobalFunc(param)
    " Make fix missing a: easy
    echo param
endfunction
