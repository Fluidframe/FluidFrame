from fluidframe.styling.base_stylings import Style
from typing import List, Dict, Union, Optional, Tuple



class TailwindStyle(Style):
    def __init__(self, theme: str | None = None) -> None:
        super().__init__(theme, "tailwind")
        
    def font(self, size: Optional[Union[str, int, float]] = None, 
            weight: Optional[Union[str, int]] = None, 
            family: Optional[str] = None,
            style: Optional[str] = None,
            variant: Optional[str] = None,
            line_height: Optional[Union[str, int, float]] = None,
            color: Optional[Union[str, Tuple[int, int, int], Dict[str, int]]] = None) -> str:
        styles = []
        if size:
            if isinstance(size, (int, float)):
                styles.append(f"text-[{size}px]")
            else:
                sizes = {"xs": "text-xs", "sm": "text-sm", "base": "text-base", 
                         "lg": "text-lg", "xl": "text-xl", "2xl": "text-2xl"}
                styles.append(sizes.get(size, f"text-[{size}]"))
        if weight:
            if isinstance(weight, int):
                styles.append(f"font-[{weight}]")
            else:
                weights = {"thin": "font-thin", "normal": "font-normal", 
                           "medium": "font-medium", "bold": "font-bold"}
                styles.append(weights.get(weight, f"font-{weight}"))
        if family:
            families = {"sans": "font-sans", "serif": "font-serif", "mono": "font-mono"}
            styles.append(families.get(family, f"font-[{family}]"))
        if style:
            styles.append("italic" if style == "italic" else "not-italic")
        if variant:
            styles.append("small-caps" if variant == "small-caps" else "normal-case")
        if line_height:
            styles.append(f"leading-[{line_height}]")
        if color:
            styles.append(self._parse_color('text', color))
        return " ".join(styles)

    def layout(self, margin: Optional[Union[str, int, Tuple[Union[str, int], ...]]] = None,
            padding: Optional[Union[str, int, Tuple[Union[str, int], ...]]] = None,
            width: Optional[Union[str, int, float]] = None, 
            height: Optional[Union[str, int, float]] = None,
            display: Optional[str] = None,
            position: Optional[str] = None,
            background: Optional[Union[str, Tuple[int, int, int], Dict[str, int]]] = None,
            opacity: Optional[Union[float, int]] = None) -> str:
        styles = []
        if margin:
            styles.append(self._parse_spacing('m', margin))
        if padding:
            styles.append(self._parse_spacing('p', padding))
        if width:
            styles.append(f"w-[{width}]" if isinstance(width, (int, float)) else f"w-{width}")
        if height:
            styles.append(f"h-[{height}]" if isinstance(height, (int, float)) else f"h-{height}")
        if display:
            styles.append(display)
        if position:
            styles.append(position)
        if background:
            styles.append(self._parse_color('bg', background))
        if opacity is not None:
            opacity_value = int(opacity * 100) if isinstance(opacity, float) else opacity
            styles.append(f"opacity-{opacity_value}")
        return " ".join(styles)
    
    def flex(self, direction: Optional[str] = None, 
            justify: Optional[str] = None, 
            align: Optional[str] = None, 
            wrap: Optional[str] = None,
            grow: Optional[Union[str, int]] = None,
            shrink: Optional[Union[str, int]] = None,
            basis: Optional[Union[str, int]] = None) -> str:
        styles = ["flex"]
        if direction:
            styles.append(f"flex-{direction}")
        if justify:
            styles.append(f"justify-{justify}")
        if align:
            styles.append(f"items-{align}")
        if wrap:
            styles.append(f"flex-{wrap}")
        if grow is not None:
            styles.append(f"flex-grow-{grow}" if isinstance(grow, int) else "flex-grow")
        if shrink is not None:
            styles.append(f"flex-shrink-{shrink}" if isinstance(shrink, int) else "flex-shrink")
        if basis is not None:
            styles.append(f"flex-basis-[{basis}]" if isinstance(basis, int) else f"flex-basis-{basis}")
        return " ".join(styles)
    
    def border(self, width: Optional[Union[str, int]] = None, 
            color: Optional[Union[str, Tuple[int, int, int], Dict[str, int]]] = None, 
            style: Optional[str] = None, 
            radius: Optional[Union[str, int]] = None) -> str:
        styles = []
        if width is not None:
            styles.append(f"border-[{width}px]" if isinstance(width, int) else f"border-{width}")
        if color:
            styles.append(self._parse_color('border', color))
        if style:
            styles.append(f"border-{style}")
        if radius is not None:
            styles.append(f"rounded-[{radius}px]" if isinstance(radius, int) else f"rounded-{radius}")
        return " ".join(styles)

    def spacing(self, gap: Optional[Union[str, int]] = None, 
            space_x: Optional[Union[str, int]] = None, 
            space_y: Optional[Union[str, int]] = None) -> str:
        styles = []
        if gap is not None:
            styles.append(f"gap-[{gap}px]" if isinstance(gap, int) else f"gap-{gap}")
        if space_x is not None:
            styles.append(f"space-x-[{space_x}px]" if isinstance(space_x, int) else f"space-x-{space_x}")
        if space_y is not None:
            styles.append(f"space-y-[{space_y}px]" if isinstance(space_y, int) else f"space-y-{space_y}")
        return " ".join(styles)


    def _parse_spacing(self, prefix: str, value: Union[str, int, Tuple[Union[str, int], ...]]) -> str:
        if isinstance(value, (str, int)):
            return f"{prefix}-[{value}]" if isinstance(value, int) else f"{prefix}-{value}"
        elif isinstance(value, tuple):
            return " ".join([f"{prefix}{side}-[{v}]" if isinstance(v, int) else f"{prefix}{side}-{v}" 
                             for side, v in zip(['t', 'r', 'b', 'l'], value)])

    def _parse_color(self, prefix: str, color: Union[str, Tuple[int, int, int], Dict[str, int]]) -> str:
        if isinstance(color, str):
            return f"{prefix}-{color}" if color.startswith('#') else f"{prefix}-[{color}]"
        elif isinstance(color, tuple):
            return f"{prefix}-[rgb({','.join(map(str, color))})]"
        elif isinstance(color, dict):
            return f"{prefix}-[rgb({color.get('r', 0)},{color.get('g', 0)},{color.get('b', 0)})]"

    def apply_theme(self) -> str:
        return "bg-gray-900 text-white" if self.theme == "dark" else "bg-white text-gray-900"