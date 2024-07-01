const editItemListHTML = `
        <div class="edit-item__container">
            <div class="edit-item__top-section">
                <div class="edit-item__item-name">
                    <input type="text" pygr="edit-item__item-name">
                </div>
                <div class="edit-item__save-button">
                    <button pygr="edit-item__save-button">Save</button>
                </div>
                <div class="edit-item__cancel-button">
                    <button pygr="edit-item__cancel-button">Cancel</button>
                </div>
                <div class="edit-item__delete-button">
                    <img src="/static/img/delete.png" alt="Delete">
                </div>
            </div>
            <div class="edit-item__mid-section">
                <div class="edit-item__xpath-value">
                    <textarea name="xpath-value" pygr="xpath-value"></textarea>
                    <span>Selection Count: <span pygr="selection-count">0</span></span>
                    <span pygr="valid-or-invalid-xpath">Invalid Xpath</span>
                </div>
                <div class="edit-item__xpath-result">
                    <div class="edit__item-apply-button">
                        <button pygr="apply-xpath">Apply</button>
                    </div>
                </div>
            </div>
            <div class="edit-item__bottom-section">
                <div class="edit-item__bottom-section-tabs">
                    <div class="tab selected">
                        <button pygr="properties-tab">Properties</button>
                    </div>
                    <div class="tab-separator"></div>
                </div>
                <div class="edit-item__bottom-section-tabs-content">
                    <div class="edit-item__properties-tab-content" pygr="properties-tab-content" style="display: none;"></div>
                </div>
            </div>
        </div>
`

const editGrabberHTML = `
        <div class="edit-item__container">
            <div class="edit-item__top-section">
                <div class="edit-item__item-name">
                    <input type="text" pygr="edit-item__item-name">
                </div>
                <div class="edit-item__save-button">
                    <button pygr="edit-item__save-button">Save</button>
                </div>
                <div class="edit-item__cancel-button">
                    <button pygr="edit-item__cancel-button">Cancel</button>
                </div>
                <div class="edit-item__delete-button">
                    <img src="/static/img/delete.png" alt="Delete">
                </div>
            </div>
            <div class="edit-item__mid-section">
                <div class="edit-item__xpath-value">
                    <textarea name="xpath-value" pygr="xpath-value"></textarea>
                    <span>Selection Count: <span pygr="selection-count">0</span></span>
                    <span pygr="valid-or-invalid-xpath">Invalid Xpath</span>
                </div>
                <div class="edit-item__xpath-result">
                    <div class="edit-item__attribute-selector">
                        <label for="selected-attribute">Attribute</label>
                        <select id="selected-attribute" pygr="selected-attribute">
                            <option value="text">Text</option>
                        </select>
                    </div>
                    <div class="edit__item-apply-button">
                        <button pygr="apply-xpath">Apply</button>
                    </div>
                </div>
            </div>
            <div class="edit-item__bottom-section">
                <div class="edit-item__bottom-section-tabs">
                    <div class="tab selected">
                        <button pygr="data-tab">Data</button>
                    </div>
                    <div class="tab">
                        <button pygr="properties-tab">Properties</button>
                    </div>
                    <div class="tab-separator"></div>
                </div>
                <div class="edit-item__bottom-section-tabs-content">
                    <div class="edit-item__data-tab-content" pygr="data-tab-content">
                        <div class="edit-item__grabbed-input-data"><textarea id="grabbed-input-data" pygr="grabbed-input-data"></textarea></div>
                        <div class="edit-item__grabbed-output-data"><textarea id="grabbed-output-data" pygr="grabbed-output-data"></textarea></div>
                        <div class="edit-item__transform-button"><button pygr="transform-button">Transform</button></div>
                    </div>
                    <div class="edit-item__properties-tab-content" pygr="properties-tab-content" style="display: none;"></div>
                </div>
            </div>
        </div>
`

const editNavigationHTML = `
        <div class="edit-item__container">
            <div class="edit-item__top-section">
                <div class="edit-item__item-name">
                    <input type="text" pygr="edit-item__item-name">
                </div>
                <div class="edit-item__save-button">
                    <button pygr="edit-item__save-button">Save</button>
                </div>
                <div class="edit-item__cancel-button">
                    <button pygr="edit-item__cancel-button">Cancel</button>
                </div>
                <div class="edit-item__delete-button">
                    <img src="/static/img/delete.png" alt="Delete">
                </div>
            </div>
            <div class="edit-item__mid-section">
                <div class="edit-item__xpath-value">
                    <textarea name="xpath-value" pygr="xpath-value"></textarea>
                    <span>Selection Count: <span pygr="selection-count">0</span></span>
                    <span pygr="valid-or-invalid-xpath">Invalid Xpath</span>
                </div>
                <div class="edit-item__xpath-result">
                    <div class="edit-item__attribute-selector">
                        <label for="selected-attribute">Attribute</label>
                        <select id="selected-attribute" pygr="selected-attribute">
                            <option value="text">Text</option>
                        </select>
                    </div>
                    <div class="edit__item-apply-button">
                        <button pygr="apply-xpath">Apply</button>
                    </div>
                </div>
            </div>
            <div class="edit-item__bottom-section">
                <div class="edit-item__bottom-section-tabs">
                    <div class="tab selected">
                        <button pygr="data-tab">Data</button>
                    </div>
                    <div class="tab">
                        <button pygr="navigation-tab">Navigation</button>
                    </div>
                    <div class="tab">
                        <button pygr="properties-tab">Properties</button>
                    </div>
                    <div class="tab-separator"></div>
                </div>
                <div class="edit-item__bottom-section-tabs-content">
                    <div class="edit-item__data-tab-content" pygr="data-tab-content">
                        <div class="edit-item__grabbed-input-data"><textarea id="grabbed-input-data" pygr="grabbed-input-data"></textarea></div>
                        <div class="edit-item__grabbed-output-data"><textarea id="grabbed-output-data" pygr="grabbed-output-data"></textarea></div>
                        <div class="edit-item__transform-button"><button pygr="transform-button">Transform</button></div>
                    </div>
                    <div class="edit-item__properties-tab-content" pygr="properties-tab-content" style="display: none;"></div>
                    <div class="edit-item__navigation-tab-content" pygr="navigation-tab-content" style="display: none;">
                        <div class="edit-item__navigation-type-selector">
                            <label for="navigation-type">Type</label>
                            <select id="navigation-type">
                                <option value="load-url">Load URL</option>
                                <option value="click">Click</option>
                            </select>
                        </div>
                        <div class="edit-item__wait-times">
                            <div class="edit-item__wait-before">
                                <span>Pause </span>
                                <input type="number" pygr="pause-before-seconds" value="0">
                                <span>seconds before execution</span>
                            </div>
                            <div class="edit-item__wait-after">
                                <span>Pause </span>
                                <input type="number" pygr="pause-after-seconds" value="0">
                                <span>seconds after execution</span>
                            </div>
                            <span class="edit-item__pauses-title">Pauses</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
`

const itemNavigationHTML = `
    <div class="item navigation" pygr="item-type-navigation">
        <div class="item-info">
            <div class="item-type"><span>Navigation</span></div>
            <div class="type-name-separator"></div>
            <div class="item-name"><span pygr="item-name">LoadMaxProds</span></div>
        </div>
    </div>
`

const itemItemListHTML = `
    <div class="item item-list" pygr="item-type-item-list">
        <div class="item-info">
            <div class="item-type"><span>ItemList</span></div>
            <div class="type-name-separator"></div>
            <div class="item-name"><span pygr="item-name">Item List</span></div>
        </div>
        <div class="item-list-children"></div>
    </div>
`

const itemGrabberHTML = `
    <div class="item grabber" pygr="item-type-grabber">
        <div class="item-info">
            <div class="item-type"><span>Grabber</span></div>
            <div class="type-name-separator"></div>
            <div class="item-name"><span pygr="item-name">id</span></div>
        </div>
    </div>
`