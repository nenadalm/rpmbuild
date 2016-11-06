set nocompatible
filetype off
colorscheme desert
let g:phpcomplete_parse_docblok_comments = 1

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

"plugin manager
Plugin 'gmarik/Vundle.vim'
"rst plugin
Plugin 'Rykka/riv.vim'
"rst instant preview
Plugin 'Rykka/InstantRst'
"better completion for php
Plugin 'shawncplus/phpcomplete.vim'
"rainbow parenthesis
Plugin 'losingkeys/vim-niji'
"file browser
Plugin 'scrooloose/nerdtree'
"fuzzy search
Plugin 'kien/ctrlp.vim'
"tab completion during search using "/"
Plugin 'vim-scripts/Searchcomplete'
"highlights modified/new lines
Plugin 'airblade/vim-gitgutter'
"git wrapper
Plugin 'tpope/vim-fugitive'
"comments
Plugin 'scrooloose/nerdcommenter'
"surround
Plugin 'tpope/vim-surround'
"clojure repl
Plugin 'tpope/vim-fireplace'
Plugin 'tpope/vim-classpath'
"improved omnicompletion
Plugin 'AutoComplPop'

call vundle#end()

filetype plugin indent on
au BufNewFile,BufRead *.cljc set filetype=clojure

highlight clear SignColumn

"gvim
set guioptions-=m
set guioptions-=T

set number
set wildmenu
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab
set laststatus=2
set backspace=indent,eol,start
set history=100
set mouse=a
set noswapfile
set incsearch
set completeopt=menuone,longest,preview

noremap <C-S-PageDown> :tabm +1<cr>
noremap <C-S-PageUp> :tabm -1<cr>
inoremap <expr> <cr> pumvisible() ? '<C-e><cr>' : '<cr>'
inoremap <expr> <C-n> pumvisible() ? '<C-n>' : '<C-n><C-r>=pumvisible() ? "\<lt>Down>" : ""<CR>'

command! Figwheel :Piggieback! (do (require 'figwheel-sidecar.repl-api) (figwheel-sidecar.repl-api/cljs-repl))

syntax on

