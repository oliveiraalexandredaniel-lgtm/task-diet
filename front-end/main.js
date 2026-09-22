// URL base da API FastAPI (Backend)
const API_BASE_URL = 'http://127.0.0.1:8000';

// Elementos do DOM
const recipesContainer = document.getElementById('recipes-container');
const searchInput = document.getElementById('search-input');
const resultsCount = document.getElementById('results-count');
const tagButtons = document.querySelectorAll('.tag-btn');

// Estado local para armazenar todas as receitas carregadas da API
let allRecipes = [];
let selectedTag = 'todas';

// 1. Função para carregar as receitas da API (backend FastAPI)
async function fetchRecipes() {
  try {
    const response = await fetch(`${API_BASE_URL}/recipes/`);
    if (!response.ok) {
      throw new Error(`Erro na requisição: ${response.status}`);
    }
    allRecipes = await response.json();
    renderRecipes();
  } catch (error) {
    console.error('Erro ao buscar receitas:', error);
    recipesContainer.innerHTML = `
      <div class="error-message">
        <p>⚠️ Não foi possível carregar as receitas. Verifique se o servidor backend está rodando em <code>${API_BASE_URL}</code>.</p>
      </div>
    `;
  }
}

// 2. Função para renderizar as receitas na tela de forma dinâmica
function renderRecipes() {
  const searchTerm = searchInput.value.toLowerCase().trim();

  // Filtra por termo de busca e tag selecionada
  const filteredRecipes = allRecipes.filter(recipe => {
    // Filtro de Texto (Nome ou descrição se existir)
    const matchesSearch = recipe.title.toLowerCase().includes(searchTerm);

    // Filtro por Tag de Restrição
    let matchesTag = true;
    if (selectedTag !== 'todas') {
      if (Array.isArray(recipe.tags)) {
        matchesTag = recipe.tags.some(tag => 
          tag.toLowerCase().replace(/\s+/g, '_') === selectedTag ||
          tag.toLowerCase() === selectedTag
        );
      } else if (typeof recipe.tags === 'string') {
        matchesTag = recipe.tags.toLowerCase().includes(selectedTag);
      } else {
        matchesTag = false;
      }
    }

    return matchesSearch && matchesTag;
  });

  // Atualiza o contador de resultados
  if (resultsCount) {
    resultsCount.textContent = `${filteredRecipes.length} resultado(s)`;
  }

  // Limpa o container
  recipesContainer.innerHTML = '';

  // Exibe mensagem caso nenhuma receita seja encontrada
  if (filteredRecipes.length === 0) {
    recipesContainer.innerHTML = `
      <div class="no-results">
        <p>Nenhuma receita encontrada para os filtros selecionados.</p>
      </div>
    `;
    return;
  }

  // Constrói os cards dinamicamente
  filteredRecipes.forEach(recipe => {
    const card = document.createElement('div');
    card.classList.add('card');

    // Formatação de tags para renderizar no card
    const tagsList = Array.isArray(recipe.tags) 
      ? recipe.tags 
      : (recipe.tags ? recipe.tags.split(',') : []);

    const tagsHtml = tagsList
      .map(tag => `<span class="card-tag">${tag.trim()}</span>`)
      .join('');

    // Imagem da receita com fallback caso venha vazia
    const imgUrl = recipe.image_url ? recipe.image_url : 'https://via.placeholder.com/400x200?text=Sem+Foto';

    card.innerHTML = `
      <div class="card-header">
        <img src="${imgUrl}" alt="${recipe.title}" class="recipe-img">
        <div class="card-tags-badge">${tagsHtml}</div>
      </div>
      <div class="card-body">
        <h3>${recipe.title}</h3>
        <p class="prep-time">⏱️ Tempo de preparo: ${recipe.prep_time || 'N/I'} min</p>
        <button class="btn-details" onclick="showRecipeDetails(${recipe.id})">Ver Modo de Preparo</button>
      </div>
    `;

    recipesContainer.appendChild(card);
  });
}

// 3. Função para buscar e exibir os detalhes completos da receita (US02)
async function showRecipeDetails(recipeId) {
  try {
    const response = await fetch(`${API_BASE_URL}/recipes/${recipeId}`);
    if (!response.ok) throw new Error('Receita não encontrada.');
    
    const recipe = await response.json();
    
    // Formata os ingredientes
    let ingredientsListHtml = '<li>Ingredientes não especificados.</li>';
    if (recipe.ingredients && recipe.ingredients.length > 0) {
      ingredientsListHtml = recipe.ingredients
        .map(ing => `<li><strong>${ing.name}</strong>: ${ing.amount || ing.quantity || ''} ${ing.unit || ''}</li>`)
        .join('');
    }

    // Modal simples
    const modalHtml = `
      <div class="modal-overlay" id="recipe-modal" onclick="closeModal(event)">
        <div class="modal-content" onclick="event.stopPropagation()">
          <button class="modal-close" onclick="closeModalDirect()">&times;</button>
          <h2>${recipe.title}</h2>
          <p class="prep-time">⏱️ Tempo de preparo: ${recipe.prep_time || 'N/I'} min</p>
          
          <h4>🛒 Ingredientes:</h4>
          <ul>${ingredientsListHtml}</ul>
          
          <h4>👨‍🍳 Modo de Preparo:</h4>
          <p class="instructions" style="white-space: pre-line;">${(recipe.instructions || recipe.preparation_method || 'Modo de preparo não informado.').replace(/\\n|\n/g, '<br>')}</p>
        </div>
      </div>
    `;

    // Remove modal anterior se existir
    const existingModal = document.getElementById('recipe-modal');
    if (existingModal) existingModal.remove();

    document.body.insertAdjacentHTML('beforeend', modalHtml);
  } catch (error) {
    alert('Erro ao carregar os detalhes da receita: ' + error.message);
  }
}

// Função para fechar o modal
function closeModal(event) {
  if (event.target.id === 'recipe-modal') {
    closeModalDirect();
  }
}

function closeModalDirect() {
  const modal = document.getElementById('recipe-modal');
  if (modal) modal.remove();
}

// 4. Event Listeners para busca e filtros de tags
if (searchInput) {
  searchInput.addEventListener('input', renderRecipes);
}

tagButtons.forEach(button => {
  button.addEventListener('click', () => {
    // Remove a classe ativa de todos e adiciona no clicado
    tagButtons.forEach(btn => btn.classList.remove('active'));
    button.classList.add('active');

    // Obtém a tag do atributo data-tag
    selectedTag = button.getAttribute('data-tag').toLowerCase();
    renderRecipes();
  });
});

// Inicialização: carrega as receitas assim que a página abre
document.addEventListener('DOMContentLoaded', fetchRecipes);